![A test image](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

# Project: AirBnB Clone


This is the first step towards building your first full web application: the  **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## The Console

 Will be used to be able to manage the objects of our project:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object


## How to execute
There is no need to compile the file but in order for it to become an executable file permissions have to be granted.
Example:

     $ chmod 755 console.py`
     $ ./console.py                 

## Commands included in the console and how to use them
* Execute the file ```./console.py```
* Run the following commands

| Command | Function  |
|--|--|
|`help`  | Provides information about the command |
|`quit`  | Quits the console |
|`create`  | Creates a new instance of `BaseModel` |
|`show`| Prints the string representation of an instance based on the class name|
|`destroy` | Deletes an instance based on the class name and `id`|
|`all` | Prints all string representation of all instances based or not on the class name |
|`update` | Updates an instance based on the class name and `id` by adding or updating attribute |

Along with the basic commands for complete functionality it has to be used with the following objects.

|Objects|Function  |
|--|--|
| `User`| Name and other iformation about the user |
| `State`  | State where the City is located |
| `City`  | City in where the place is in  |
| `Amenity`  | What features the place has |
| `Place`  | Information about, in this case the hotel  |
| `Review`  | What people think of the place they stayed at |

## Executing the commands
After starting the console the following prompt will appear `(hbnb)`

The syntax to use the console is: 

    <Command> <classname> <id>

## Example:
To create a new object like a city, it goes like this: 
  

      $ (hbnb) create City
      a2324758-661d-46f0-8ac2-84e01e5c8aef
Notice we don't use the `<id>` when using the `create` command, we don't use it either with `help` or `quit`.

If we use any other command:

    $ (hbnb) destroy City a2324758-661d-46f0-8ac2-84e01e5c8aef
    $ (hbnb)

## Authors

Javier Cañon | [https://github.com/untaljacko](https://github.com/untaljacko)

Javier Gutierrez  | [https://github.com/JavierGutierrezC](https://github.com/JavierGutierrezC)
