# WorkoutProject1
This program imports the sys and pathlib module to get 4 inputs from the command line. It takes two arguments at index [2] and [3] which are .txt files and encrypts the message from the first file and writes the encrypted message on the second file. To encrypt the message, the program takes the first file and line by line reverses the message. Then, using the reverse() method, reverses the entire list containing the reversed lines, joins them, and returns the output to then be written on the encrypted file. Then, the program reads the encrypted file line by line to the user.

To utilize this program, the arguments at index [2] and [3] must be in .txt files and in the same directory as the program.
