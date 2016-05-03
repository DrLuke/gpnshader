# Network
This document outlines the network protocol used by gpnshader.

## Bare Essentials
Communication happens by exchanging json schemas via TCP. Every schema must contain the following keywords in the topmost object:

#### `msgid (int)`
Unique message ID generated with the python 3 [uuid library](https://docs.python.org/3/library/uuid.html#uuid.uuid1), and then [converted](https://docs.python.org/3/library/uuid.html#uuid.UUID.int) to an integer.  
The msgid can be used to reference messages in a reply to commands. This way even delayed replies can still be correlated with the original request. This in turn means that all messages that expect a reply must store their original request for a reasonable amount of time (e.g. 1 minute).

#### `status (string)`
The status of a message is a quick way to indicate success or failure of anything. Valid values for status are:  
* `ok`: Used to indicate that no problems are present, everything is fine.
* `error`: Something went wrong, check `message` for a human readable errormessage.
* `command`: This message is a command and thus must have the `command` and `monitor` keywords set to valid values.
* `reply`: This message is a reply for a previous request. Replies must have `refid` set.

## Additional Keywords

#### `refid (int)`
A msgid this message is a reply to.

#### `message (string)`
A human readable string containing information about the status of things. This could, for example, tell the user why something failed.

#### `command (object)`
This is an object that will be passed to the correct glfw-object in the worker. The command object MUST contain a `monitor (string)` keyword so that the worker knows which monitor the command goes to.

## Command Types
This segment describes different command schemas that can be sent from the controller to the workers

### Worker Commands
Command Schemas exchanges between the controller and worker that are meant directly for the Worker. An example for such a message would be a request to list all availabe monitors.

### GLFW Commands
Command schemas exchanged between the controller and glfw-workers.

#### `monitor (string)`
GLFW commands must have the monitor keyword set, otherwise they won't be recognized as such. The value must be the name of the GLFW worker's monitor you want to address (e.g. 'DVI-I-1').
If a worker doesn't exist for this monitor yet, a worker will be created. If the intent is to create a new worker, `monitor` should be the only keyword set, as any other commands will be discarded anyway.

#### `sheet (object)`
This contains the sheet this worker shall be running. It looks at the IDs of old and new nodes, and keeps objects with identical IDs. Objects whose ID isn't present in a new sheet will be deleted, while new objects will be generated for new IDs.  
If `sheet` is set, all other commands in this message will be ignored.