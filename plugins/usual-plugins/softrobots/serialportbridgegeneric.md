# SerialPortBridgeGeneric

Send data (ex: force, displacement, pressure…) through the usb port. 
Usually used to send data to an Arduino card to control the real robot.


__Target__: `SoftRobots`

__namespace__: `#!c++ softrobots::controller`

__parents__: 

- `#!c++ Controller`

__categories__: 

- Controller

Data: 

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Default value</th>
    </tr>
</thead>
<tbody>
	<tr>
		<td>name</td>
		<td>
object name
</td>
		<td>unnamed</td>
	</tr>
	<tr>
		<td>printLog</td>
		<td>
if true, emits extra messages at runtime.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>tags</td>
		<td>
list of the subsets the objet belongs to
</td>
		<td></td>
	</tr>
	<tr>
		<td>bbox</td>
		<td>
this object bounding box
</td>
		<td></td>
	</tr>
	<tr>
		<td>componentState</td>
		<td>
The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
</td>
		<td>Undefined</td>
	</tr>
	<tr>
		<td>listening</td>
		<td>
if true, handle the events, otherwise ignore the events
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>handleEventTriggersUpdate</td>
		<td>
Event handling frequency controls the controller update frequency
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>port</td>
		<td>
Serial port name
</td>
		<td></td>
	</tr>
	<tr>
		<td>baudRate</td>
		<td>
Transmission speed
</td>
		<td></td>
	</tr>
	<tr>
		<td>packetOut</td>
		<td>
Data to send: vector of unsigned char, each entry should be an integer between 0 and header-1 &lt;= 255.
The value of 'header' will be sent at the beginning of the sent data,
enabling to implement a header research in the 'receiving' code, for synchronization purposes.

</td>
		<td></td>
	</tr>
	<tr>
		<td>packetIn</td>
		<td>
Data received: vector of unsigned char, each entry should be an integer between 0 and header-1 &lt;= 255.
</td>
		<td></td>
	</tr>
	<tr>
		<td>header</td>
		<td>
Vector of unsigned char. Only one value is espected, two values if splitPacket = 1.
</td>
		<td>255 254</td>
	</tr>
	<tr>
		<td>size</td>
		<td>
Size of the arrow to send. Use to check sentData size. 
Will return a warning if sentData size does not match this value.
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>precise</td>
		<td>
If true, will send the data in the format [header[0],[MSB,LSB]*2*size]
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>splitPacket</td>
		<td>
If true, will split the packet in two for lower error rate (only in precise mode),
data will have the format [header[0],[MSB,LSB]*size],[header[1],[MSB,LSB]*size]
</td>
		<td>0</td>
	</tr>
	<tr>
		<td>redundancy</td>
		<td>
Each packet will be send that number of times (1=default)
</td>
		<td>1</td>
	</tr>
	<tr>
		<td>receive</td>
		<td>
If true, will read from serial port (timeOut = 10ms)
</td>
		<td>0</td>
	</tr>

</tbody>
</table>

Links: 

| Name | Description |
| ---- | ----------- |
|context|Graph Node containing this object (or BaseContext::getDefault() if no graph is used)|
|slaves|Sub-objects used internally by this object|
|master|nullptr for regular objects, or master object for which this object is one sub-objects|



