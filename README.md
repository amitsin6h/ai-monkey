# AI Monkey
AI Monkey supposed to be an AI based web browser but for the time it’s a web application. 
This project aims to provide user an consultant which not only answers the search query but also guide them at the same time. 
AI Monkey has two options i.e., 
1.Go Google and 
2. Go AI Monkey , 
the use of these two options are to let the user know how AI Monkey could be great for one who need a direct answer to a 
particular search query, the AI monkey works in such manner that it shows that it is consulting the user. 
AI Monkey is secured by face recognition using machine learning and also includes parts of speech production 
and voice recognition using javascript modules. It also uses plotly an python module which shows interactive graphs.

## How to use
>
  1.Make sure you have python2 installed as this project uses python2
  
  2.Make sure have pip installed
  
  3.Make sure have virtualenv installed
  
      if not:
        Try the below steps
          For Windows (run this command as adminstrator):
             pip install virtualenv
          For Linux:
              pip install virtualenv
  
  4.Clone or download the project
  
    Once the project has been downloaded and then cd into the project folder. 
    After this we will create our virtual environment, see > Step 5
  
  5.Create and activate virtualenv
  
      This shoud be done inside the project folder  
      
       For windows:
         a) Creating virtualenv 
            virtualenv env (this will create your virtual environment named env)
            
         b) Activate virtualenv
            env\Scripts\activate (simple enter the path of activate file)
            
       For Linux:
         a) Creating virtualenv 
            virtualenv env (this will create your virtual environment named env)
            
         b) Activate virtualenv
            source env/bin/activate (call the activate script)
                 
  
  
  6. After activating the virtualenv install all the required modules present in requirements.txt
  
          pip install -r requirements.txt
      
  7. Once done run the app.py file using
         
         python app.py
         
  Now you will see your server running copy the url in browser and load it you will see AI Monkey.
  
  **Note: Please use Google chrome as voice production may not work in firefox.**
