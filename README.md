# Knitted  
a full stack Ecommerce project for the "python fullstack developer course" at the jhonbryce academy.  

## general info  
the main theam for this project is an ecommerce shop selling knitted dolls, hand made.  

server side uses python django framework with rest-api interface.  
clinte side is react js with redux.  
  
##  
to run this project(windows):  
(you need to have python installed)   
activate a server side on your local machine:  
open shell in a folder made for this project then run the comands below line by line  
  
git clone https://github.com/daskalidan/Ecommers_project.git  
cd .\Ecommers_project\back\  

pip install virtualenv  
py -m venv venv  
.\venv\Scripts\activate  

pip install -r .\requirements.txt  
py .\manage.py runserver  
  
when you have a running server...  
  
open browser on this link:  
https://ecom-front.web.app/  

super user: theboss  
password: abc123  
  
or serve front side on your local machine:  
(you need to have node.js installed)  
open shell in a folder made for this project (same folder from the server side) then run the comands below line by line  
  
cd .\Ecommers_project\front\knitted_front\  
npm i  
npm start  
  
if browser does not open automaticaly open it on http://localhost:3000/  


<!-- ## app's components(front):
header: always shown on page top woth shop name and logo in the middle.
footer: at the bottom of each page with copiryte and contact us link
### main page:
left 4/12:
a user status container - displaying (guest/ user name if loged) and login/logout/register links.
a cart container - display the product chosen to cart with total price and a link to checkout page. 
an item of the week container - display an img of item of the week with special price and an add to cart button.
right 8/12: 
cards for each product (4 in a row) 
each card  name, price, how many in stock and add to cart button(only if available in stock) under an image of the product.

### login page
header, footer same as main page - main section form with: user name, password, submit button all centered.

### register page
header, footer same as main page - main section: form with user name, email, password, shipping adress, type(customer/ stuff) and submit.

### checkout page


### contact/ about
header, footer same as main page - main section: all centerd, title shop name, shop's description/about, contact phone number, contact email, fisical adress, small map showing the adress. 

## data models(back)

### product model
### inventory model
### user model
### cart model
### purches model -->


<!-- # Getting Started with Create React App and Redux

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app), using the [Redux](https://redux.js.org/) and [Redux Toolkit](https://redux-toolkit.js.org/) template.

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/). -->
