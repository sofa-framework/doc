## Help-list to make your code compile with a recent checkout from master

You made a recent checkout from master and your private plugins does not compile anymore.

This is an unconfortable situation and a lot of effort are done to reduce the amount of time this happen. But whatever care are taken, this will happen in two cases.

First cases is when breaking stuffs that shouldn't be there have been merge by mistake. Well, we apologize for this situation. To help, do not hesitate to participate in the reviewing of the PRs before they are merged into master to detect this situation.

Second case, is when breaking change that are accepted on purpose. The reason is that there is a general consensus that Sofa is currently very "fat" and thus PRs trying to clean or make sofa lightweight to compile are positive contribution to Sofa. The drawback of that is that cleaning and modularizing Sofa have a strong impact on file/code organization and for sure is going to break external code.

As this is going to happen I suggest in the following thread to report what he had to do to compile master when encountered a broken compilation. Anyone can contribute...

Hope this will help.

eg:

- I had to add a lot of #include to avoid compilation problem with xxx
- Component from #include have moved and been renamed ! I had to update my
- CMakeList.txt to add find_package(SofaImplicitField) or find_package(SofaDistanceGrid)

________________________________________________________


No contribution in this list yet. Add yours now by editing the page!
