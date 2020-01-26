# MARVEL ASSIGNMENT


I have completed this Assignment using Python and for API requests I used requests library.

#### `Approach:`

I went through the API documentation and I figured out the API urls to which I will use in my assignment. In order to use the API I have to generate the Authorization Keys, Going further I came to know it need a hash key which is the combination of public and private key and the current timestamp using md5 algorithm. In my project there are four sub folders are as follow:

##### `Config:` It has the two files one is the base.conf file and the other is stage.conf file. Base config will have the configuration which will have the configuration data that will remain same across all users and environment. For example the API urls and some other data. Where as stage.conf is user specific or environment specific.


`Lib:` It has all the functions which we can reuse in our testcases. Some of the functions are as follow.


`_get_character_id_with_description:_` Function to get character with description. First part of the first question can be achieved by this. 

`_get_series_with_character_id_ :` Function to get the series using character_id. Passing the list of character_id which we have got from the `get_character_id_with_description` will solve the second part of the first question.

`_get_list_of_characters_in_series:_` This function is used solve the second question in the list. We can get the list of series from the function `get_series_with_character_id` using random() function will send two random list to the function and it will give the characters present from the series list.

`_get_list_of_stories_with_character_without_description:_ ` This function will solve the third question. We will pass the list of characters which has description from the function `get_character_id_with_description:`. Once we get the list of stories we will traverse through each story and get the characters from each story and check if the charaters present in the story is present in the list of characters without description. If its present then will not print the stories else will print.


**`TestCase:`** It has one file which has the testcases to execute. Below are the testcases.

**.** `test_get_character_id_With_Description_and_series:`  It will execute the first question of assiggnment.

**.** `test_get_list_of_characters_with_description_in_two_series`: It will execute the second question of assignment.

**.** `test_get_list_of_stories_with_character_without_description:` It will execute the third question of assignment.


`Framework:`

Below are the important points which I have considered while creating the framework.

1. I have used `Nose` as a unit testing framework in our project.
2. I have used `Setup and Teardown `function in our TestCases.
3. I have segregated my testcases by marking with `attribute library.` It will be helpful while running the tests that wheather we want to run our smoke testcases or functional testcases etc at run time.
4. I have used `flaky` library to rerun my failed testcases.
5. As python gives flexiblity to run your code on your local environment. I have created a local environment folder call env. It has all the dependencies which we are using in our testcases.
6. I have not done the assertion as I did not have assertion data to assert.


#### `Important Notes:`

As some request has more then 1000 results but the limit was set to 20 by default and offset was set to 0, But as in the assignment its written to get all the values. For example it has written to get all the characters which has description. I was sending the request with limit 100 and using the mathematical calculation I got the number of offset or pages and I traverse through all the offset and got the response for all the offsets. When limit was 20 it was sending a lot of request which gives the connection abort error  `raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer')) ` due to lot of request. I set the limit to 100 and it does not give that error after that.


### STEPS TO RUN THE TESTCASES:


. You can clone the git and go inside the folder. I have created a bash file to run the script.

. Run the below command:

            sh testrun.sh
            
#### `Details About testrun.sh file`

. We need to activate the environment by executing the below command.
   
    source  env/bin/activate
    
. After activating we need to execute the below command.

    nosetests --with-flaky -v --tc-file config/Base/base.conf --tc-file config/Stage/stage.conf -a type='smoke' TestCase/testcase.py
    
    Below are the details about above command:
    
       nosetests : command to execute nose unit test framework
    --with-flaky : this command line argument used to rerun the test
              -v : To run the test in vervose mode
       --tc-file : To pass the config file path  
         -a type : To pass the attribute (Tag) argument. Eg: smoke
         
      













 