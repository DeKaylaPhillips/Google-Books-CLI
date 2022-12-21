**Error Handling**

Line 26 - Search Query Errors 
- [X] *Program accounts for no input at all* [2022-12-20]
- [] Program does not yet handle typos
- [] Book numbering issues with certain inputs... indexing is correct because when selecting a book, the correct book is chosen, even if it does not properly correlate to the number of the book displayed.

Line 64 - Book Selection Errors *Fixed*
- Selection should only be successful with input numbers 0-5.
- [X] *Accounts for no book selection input.* [2022-12-20]
- [X] *Program falsely adds book to reading list when using 0 as a selection number. More than likely an indexing issue.* [2022-12-20](syntax error w/ operators corrected)
- [X] *Program needs to appropriately handle numbers above 5. Input of 6 returns IndexError.* [2022-12-20] (syntax error w/ opeerators corrected)

Line 72 - Menu Selection Errors *Fixed*
- Menu should return to search interface or reading list based on the input value.
- [X] *Program returns to search when no input value is found.* [2022-12-20]
- [X] *Program does not return to search menu when 1 is selected.* [2022-12-20] (menu_selection var casted to an integer for proper comparison of input value)
- [X] *Program does not print reading list when 2 is selected.* [2022-12-20] (menu_selection var casted to an integer for proper comparison of input value)

Reading List Errors *Fixed*
- Reading list should reflect updated status with every book a user chooses to add to the list 
- [X] *Reading list not updating with multiple selections.* [2022-12-20] (created global reading_list variable instead of local reading_list variable so list does not recreate every time the "search_books()" function is called)

Line 30 - Publisher Errors from API
- Some books do not have publishers. 
- [] Need to account for this potential error prior to displaying all data.
  