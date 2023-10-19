# Search-the-longest-compounded-word

<h1>Steps to execute code</h1>
<ul>
  <li>Your Machine must have Python 3.7 or 3.7+ installed.</li>
  <li>Download or clone the repository.</li>
  <li>Open Solution.py and enter the path to the input file in place of the placeholder address in the 'Main' block.</li>
  <li>Run the script.</li>
</ul>

<h1>Overview</h1>
<h2>Problem Statement</h2>
<p>Write a code to parse through a given input text file consisting of alphabetically sorted word list, with each word in a new line. After parsing through the list give the longest and the second longest compounded word along with the time took to process the file.</p>
<p>A compounded word is a word that cab be created by combining shorter words in the same file or list.</p>

<h2>Approach</h2>
<p>Considering this is a problem involving strings and their processing, I opted to utilize the Trie Data Structure, which is perfext for these kinds of operations on strings and substrings. My approach involved the following steps:</p>
<ul>
  <li>Create a Trie Node class.</li>
  <li>Create a Trie tree via the insertion operation to insert the words form the file, reading it line by line. At the same time checking if a word exists in the Trie acting as a prefix for the current word, and if yes then storing the current word and the suffix left over as a <u>tuple</u> in a buffer list acting as a Queue.</li>
  <li>Checking the tuples or records in the buffer Queue and seeing if the suffix can be further compounded/can be further broken down to constituent words and if they exist in the Trie.</li>
  <li>If the suffix is a valid word then apending the tuple containing the original word and suffix to the buffer.</li>
  <li>If a word is compounded, then check it's length and assign to longest_compounded_word and second_longest_compounded_word as required.</li>
  <li>At the end return the first and second longest compounded words and the time taken to process the files and print it.</li>
</ul>

<h1>Output</h1>

<b>For Input_01.txt file:</b><br>
<img src='https://github.com/DIGVI962/Search-the-longest-compounded-word/blob/main/Output_01.PNG'>
<br>
Benchmarked time: 0.99754 milliseconds
<p></p>
<b>For Input_02.txt file:</b><br>
<img src='https://github.com/DIGVI962/Search-the-longest-compounded-word/blob/main/Output_02.PNG'>
<br>
Benchmarked time: 1222.52867 milliseconds
