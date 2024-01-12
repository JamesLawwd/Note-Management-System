# CLI Note App (management system)



## Introduction
This is a command-line interface (CLI) application for managing notes and tags. It provides functionality to create, view, edit, and delete notes, create and manage tags, and associate notes with tags.

## Features
User Management:

-Create users
-List all user

Note Management:

-Create a new note
-List all notes for a specific user
-View a specific note by its ID
-Edit a specific note by its ID
-Delete a note by its ID

Tag Management:

-Create a new tag
-View a specific tag by its ID
-List all tags
-Edit a specific tag by its ID
-Delete a tag by its ID

Association Management:

-Associate a note with a tag
-Dissociate a note from a tag
-Get tags associated with a note
-Get notes associated with a tag

## Installation 

1. Clone this repository to your local amchine
    git clone (https://github.com/JamesLawwd/Note-Management-System)
    cd Project_CLi

2. Create a Virtual Environment
   python -m venv venv



```markdown
# Note App with CLI

## Introduction

This is a command-line interface (CLI) application for managing notes and tags. It provides functionality to create, view, edit, and delete notes, create and manage tags, and associate notes with tags.

## Features

- User Management:
  - Create users
  - List all users

- Note Management:
  - Create a new note
  - List all notes for a specific user
  - View a specific note by its ID
  - Edit a specific note by its ID
  - Delete a note by its ID

- Tag Management:
  - Create a new tag
  - View a specific tag by its ID
  - List all tags
  - Edit a specific tag by its ID
  - Delete a tag by its ID

   Association Management:
  - Associate a note with a tag
  - Dissociate a note from a tag
  

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   cd Project_CLi
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

 ```eg:
  click```

## Usage

To use the CLI, you can run the following command:

```bash
python cli.py
```

This will start the CLI interface, and you can interact with the various commands as mentioned in the Features section.

## Example Usage

### Create a User

```bash
python cli.py createuser --name JohnDoe
```

### Create a Note

```bash
python cli.py createnote --title "Meeting Notes" --content "Discussion on project updates" --user_id 1
```

### Create a Tag

```bash
python cli.py createtag --name "
```

### Associate a Note with a Tag

```bash
python cli.py associate --note_id 1 --tag_id 1
```

### Get Tags Associated with a Note

```bash
python cli.py tagsfornote --note_id 1
```

### List All Notes for a User

```bash
python cli.py listnotes --user_id 1
```

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or would like to contribute to this project, please create an issue or pull request on the [GitHub repository]((https://github.com/JamesLawwd/Note-Management-System)).

## License

MIT License

Copyright (c) [2023] [James]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Author
 [James Kinyanjui]







