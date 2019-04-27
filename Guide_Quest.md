**.quest file format**

Filename : ***id.quest***

Contents :

1. *name:* The name printed out to the player

2. *description*: The initial message the player will receive when the quest starts
3. *onStart*: Series of Event separated by the pipe character : `|` . They trigger sequentially when the quest starts.
4. *onResolve*: Series of Event separated by the pipe character : `|` . They trigger sequentially when the quest ends.
5. *steps*: Series of quest IDs separated by the pipe character : `|` . Their completion is required for this quest to be resolved. Step quests can also have steps, recursively.
6. *conditions*: Series of Condition separated by the pipe character : `|` . These are simple conditions that should all return True when met in order to complete this quest.
7. *next*: Series of quest IDs separated by the pipe character : `|` . These quests will become available as soon as this quest is resolved.

Example:

```json
name: Example Quest
description: This quest is an example. You have to create a Rock in the Parc to complete it.
onStart: RemoveEntity(Rock("Parc"))|CreateCharacter(Character("Rock_Lover","Parc",[HP(5)],{"completed_example": ["I love Rocks ! Thank you for creating this Rock.", {}]}))
onResolve: NpcToPlayer("Rock_Lover",["completed_example"])
steps: none
conditions: EntityExists(Rock("Parc"))
next: anotherQuest
```

This quest contains a lot of use cases. Let's tear them down :

**Events**

An event is an action performed by the game. Here you can see RemoveEntity performed on Start, which can be performed with any Entity. Rock is an Entity like many others. Characters are also Entities, but more complex.

The next event is CreateCharacter, which is a bit more like CreateEntity but will also generate the Character's code. It uses a Character object, which will be detailed later.

To create an Event:

 `Event(Entity())`

**Entities**

An entity is a *.py* file in the *world/* folder. It has a name and can be created or removed. If there is code in it, it might be executed as an interaction.

To create an Entity:

 `Rock("World/Path")` if the implementation of *Rock* allows it.

*World/Path* represents the folder where you cant this entity to be placed. For example "Parc/Bin" will create the entity in the `Bin` directory in the `Parc` directory, which in its turn is in the global `world` directory. The player cannot go outside of `world`.

or generally:

 `Entity("Name","World/Path")`

**Characters**

Characters are advanced Entities. They have built-in dialogue and characteristics features such as Health Points.

To create a character:

`Character("Name","World/Path",[Array of Characteristics],{Dialogues as JSON})`

This one requires more understanding of python.

*name* will be used to create a class corresponding to this unique character. There should be only one Character with this name, and it needs to respect some naming conventions : Must start with a letter (not case sensitive), can contain numbers and `-`. Any other symbol might not work.

`Array of Characteristics` is Characteristics separated by commas `,` more on this later.

`Dialogues as JSON` is a precise data structure allowing the user to interact with Characters. A special section is dedicated to this.

