# todo-response
This repository is a reponse to a very silly/poor [youtube video](https://youtu.be/9zLG-WauliY). In it, some "python" code is typed into MSNotebook to create a todo app. The app consists of:
1. a global list to hold tasks
2. a while loop
3. a way to accept keyboard input
   - "done" to exit the loop
   - a task to store
4. a way to print the todo items

The question was raised, why would one want to write a commandline to-do program like what was proposed in the linked video. I think that as a practice task it is ok, but it is more interesting as a technical interview question.

## possible motivations
### Why might a command line To-Do app be good practice?
- simple text I/O /formating- creating new records
- practice decomposing a problem

### Why I would consider asking a candidate to build one?
1. Great opportunity for a requirements discussion
   - What workflow/usecases are we supporting?
     - Should the times persist?
     - should the app remain up? (like the example) or be more Git-like?
   - What value can we provide on top of merely listing things?
     - Task duration? (as in this example)
     - various reports?
1. For a timeboxed interview, we can quickly get code working and see how a candidate structures code
   - is it maintainable?
   - Testable?
   - extensible?
   - does it demonstrate knowledge of standard libary features?
1. This task has a natural (and fairly linear) scope curve. It naturally allows very easy extensibility to gradually add many more features
   - task timing
   - task persistence
     - in a file
     - in sqlite
   - sensible command line interface
   - help capabilities
   - more advanced data models
     - associating tasks with "Accounts" and accounts with rates and creating an invoice/timesheet
     - ???
