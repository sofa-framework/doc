cmake_minimum_required(VERSION 3.14)
project(SofaDocGenerator)

find_package(Sofa.Core REQUIRED)
sofa_find_package(Sofa.Simulation.Graph REQUIRED)
sofa_find_package(TinyXML2 REQUIRED)

find_package(cxxopts 3.1 QUIET)
if(NOT cxxopts_FOUND AND SOFA_ALLOW_FETCH_DEPENDENCIES)
    message("${PROJECT_NAME}: DEPENDENCY cxxopts NOT FOUND. SOFA_ALLOW_FETCH_DEPENDENCIES is ON, fetching cxxopts...")

    include(FetchContent)
    FetchContent_Declare(cxxopts
            GIT_REPOSITORY https://github.com/jarro2783/cxxopts
            GIT_TAG        v3.1.1
    )

    FetchContent_GetProperties(cxxopts)
    if(NOT cxxopts_POPULATED)
        FetchContent_Populate(cxxopts)

        set(CXXOPTS_BUILD_EXAMPLES OFF CACHE INTERNAL "")
        set(CXXOPTS_BUILD_TESTS OFF CACHE INTERNAL "")
        set(CXXOPTS_ENABLE_INSTALL ON CACHE INTERNAL "")
        message("${PROJECT_NAME}: adding subdirectory ${cxxopts_SOURCE_DIR}")

        add_subdirectory(${cxxopts_SOURCE_DIR} ${cxxopts_BINARY_DIR})
    endif()
elseif (NOT cxxopts_FOUND)
    message(FATAL_ERROR "Sofa.GUI.Common: DEPENDENCY cxxopts NOT FOUND. SOFA_ALLOW_FETCH_DEPENDENCIES is OFF and thus cannot be fetched. Install libcxxopts-dev (version>=3.1.0), or enable SOFA_ALLOW_FETCH_DEPENDENCIES to fix this issue.")
endif()


set(SOFADOCGENERATOR_SRC "src")

set(SOURCE_FILES ${SOFADOCGENERATOR_SRC}/Main.cpp)

add_executable(${PROJECT_NAME} ${SOURCE_FILES} ${SOFADOCGENERATOR_SRC}/XMLtoPython.h)
target_link_libraries(${PROJECT_NAME} PUBLIC Sofa.Core Sofa.Simulation.Graph)
target_link_libraries(${PROJECT_NAME} PUBLIC cxxopts::cxxopts)
target_link_libraries(${PROJECT_NAME} PRIVATE tinyxml2::tinyxml2)
target_include_directories(${PROJECT_NAME} PUBLIC ${SOFADOCGENERATOR_SRC})

sofa_add_targets_to_package(
    PACKAGE_NAME Sofa.GUI
    TARGETS ${PROJECT_NAME} AUTO_SET_TARGET_PROPERTIES
    INCLUDE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}"
    INCLUDE_INSTALL_DIR "Sofa.GUI/${PROJECT_NAME}"
    )
