# Milton Bookstore 

Milton Bookstore is small business serving a local community. They have recently decided to embrace the power of ecommerce to help them scale to customers beyond the reach of their brick and mortar store. This web application will set them up for the expected future growth and provide, the not so tech savy owners, the ability to easily manage the store from the front end. The website will host a fully functioning ecommerce platform alongside a handy blog to help achieve rankings via SEO. 

## UX

The website was kept simple to allow the visitors to focus on the task at hand. The website features both a sticky header and a sticky footer. The header allows the users to easily navigate through the website including providing them a handy search bar. The sticky footer provides the visitor with useful information from the cart including the the amount they have saved by taking advantage of discounted products. The footer also hosts a large button to the checkout page acting as a constant call to action. 

### User Stories

#### Store Owner

The store owner would like to use the front end of the website to perform CRUD functionaly for the books avaialable for sale as well as the blog posts published.

Books
- Create: The store owner can log in using the superuser account credential provided. Once logged in the main navigation bar will change and reveal a new drop down menu showing a link to add a book. The link will redirect the page to a form indicating the book properties that can be added and used by the template. The store owner will also be shown what entries are required. The store owner will have the ability to set a discounted price as well a regular price.
- Read: The store owner wants to view the books available for sale. This can be achieved regardless of log in status. The top navigation bar hosts a drop down menu reading books hosting the ability to view all books or by a specific category. The navigation bar also hosts a search bar that allows the store owner to search for a keyword in the book name, description, category, and more. Once on the books page the owner can use the sorting functionality as further assistance.
- Update: The store owner can log in using the superuser account credential provided. Once logged in the store owner can look for the product that needs to be edited by simply searching in the navigation bar. Although a manual skim of the category can provide the same result, the search bar will be significantly quicker. The store owner will automatically see the edit button beside the search results. If the store owner is unsure about the book about to be edited, by clicking on the title the book details page will populate. Once it is confirmed that the book is the correct one, the edit button on the book details page can be clicked. This leads the owner to a prepopulated with the book details. Changes can be made to the form and saved.
-Delete: Much like the update scenario, once the store owner has logged in as a superuser and found the correct book using the search bar, a delete button is populated next to the edit button. It is highly recommended to visit the book details page to confirm that the correct book has been found as there is no possibility of recovering the deleted book. The book details will also host a delete button again adjacent to the edit button.

Blog
- Create: Once the store owner is logged in using a superuser account, the admin drop down menu will appear in the main navigation bar. Using the drop down link labeled add a post, the store owner will be redirected to the add a post page. This page hosts an easy to fill out form indicating the required fields. Once complete, the owner can press the button to submit and the post will be published. 
- Read: This function can be conducted regardless of log in status. The main navigation bar hosts a link to the blog. By clicking this, the user will be led to the blog page. The blog page provides a list of all the blog posts. By clicking on the title or the image of a post entry, the owner will direcred to the blog detail page for that blog post.
- Update: Once the store owner is authenticated as a superuser, the owner can use the navigation blog link to redirect to the blog page. Much like the list of products, the blog post also host an edit button beside each entry. Note that navigating to the blog detail page will also provide you with a similar edit button. Both locations of the edit button lead you to a prepopulated form with the blog post information. Changes can be made and then submitted using the form submit button.
- Delete: Much like the edit button, once the store owner is authenticated as a super user, a delete button will appear beside each blog post both on the main blog page and the blog detail page. The delete button does not request a confirmation nor is it recoverable. It is advised to use caution and ensure that the right blog post is being deleted.

The store owner may also want to visit the backend of the store to conduct some more advnaced administrative work including accessing the purchase order database. The store owner can achieve this by firstly authenticating as a superuser. Once complete, an admin drop down menu will appear in the main navigation bar. This drop down menu hosts a link to the admin backend panel. As the user is already authenticated, the link will directly populate the main admin page.

#### Visitor:

Register: The main navigation bar hosts a profile drop down menu. When no user is logged in, this will show a register button. By following this link, the visitor will be led to a registration form. By completing this form, a user account and a user profile will automatically be generated. The visitor will also be sent an email confirmation that is required to fully authenticate the account creation.

Login: The main navigation bar also hosts a login button in the profile drop down menu when no user is logged in. The link leads to a standard login page where the user can use either their username or email address to login alongside their password.

Purchase: The visitor can accumulate products on the cart. Once ready to make the purchase, the checkout button available in the footer, notifications, or the cart can be used to navigate to the payment page. This payment can be made as a registered user or as a guest. If the visitor is logged and has made a purchase in the past, the form will be populated with the default shipping and contact information. The visitor can also enter different information and then choose whether or not to update their user profile with the information in the form. A stripe credit card payment section at the bottom allows visitor to pay with a plethora of card options.

## Features

The store owner has full CRUD functionality available via the frontend for both books and blog posts.

The visitor has the ability to purchase products both as as a guest and as a registered user.

The search functionality available allows the users to search through book title, short description, full description, category, and also by the unique ISBN numbers.

The sorting fearure allows the books to be sorted by price, name, rating, and category. Whereas, the blogs can only be sorted by name and category.

The order profile page provides a clear view of the users personal account and also provides the ability to update default shipping and contact information.

The points feature allows the users to collect points on every purchase made. Each dollar earns the user 100 points. The points balance in the user profile accumulates as the user continues to shop.

The total savings feature allows the user to constantly track how much they are saving by utlizing the discounted price. This value is always present in the sticky footer acting as a constant reminder of their savings. To further assist the user in making the purchase and taking advantage of the savings, a large checkout button is also present in the sticky footer.

### Features Left to Implement

A redemption process for the accumulated points in the user profile is planned. It is not certain if the points will unlock a tiered prizing system based on points balance or provide the ability to use the points on all purchases as a payment method. 

A reviewing system for verified purchasers should be implemented allowing users that have bought the product to provide a rating out of 5 as well as leave a review for the product. This star rating should be used to calculate the rating beside the product and the review should automatically populate below the product.

A commenting system should be implemented on the blog allowing users to interact with the posts.

The homepage should host more call to actions. Also, a featured product gallery would help the visitors to navigate to the most popular products.

A more robust webhooks system needs to be implemented to bulletproof transactions made on the ecommerce store.

## Technologies used

HTML - Used to build basic content of the website
CSS - Used for complete styling of the website 
Bootstrap - Used to apply layout style to the website
JS/jQuery - Used to conduct many interactive functions on the front end of the website
Python/Django - Used to create the app
Heroku - Used to deploy the app
Postgres - Used as a database to store the data on heroku
Font Awesome - Used to insert icons on the page
All Auth - Used as an authentication platform for users on the website.
Stripe - Used to recieve payments from the users for their purchase
Whitenoise - Used to allow Heroku to load static files as AWS or a similar server was not set up
Crispy Forms - Used to style the forms in Django
Miniwebtool - Used to generate a secret key

## Testing

The forms were tested thoroughly tested to insert incorrect values but the form performed well and the database was able to handle the information correctly.

The webstie was throuhghly tested in multiple browsers (Firefox, Chrome, Edge, Safari, and IE). The website responsiveness acted correctly in all browsers.

The website was also observed in many different mobile and tablet resolution using Google Developer Tools, again acting as expected. The app is completely responsive. 

The website was tested in W3C HTML & CSS validators and no errors were realized.

## Deployment

The website was pushed to github using gitpod to maintain version control. Once the final version of the website was committed and pushed, the website was hosted using heroku and postgres as the deployment database. 

Please find the live website here: (https://usmaanmujtaba-milestone4.herokuapp.com/)

Currently the live version and development versions are identical however there are a few updrades planned for the website and will be tested in the development environment before deployment.

## Credits

### Content

All book related information inlcuding images was pulled from the Chapters Indigo online store.

### Media 

Font Awesome was used to insert icons on to the page.

The remaining banner images were found using google images.

### Acknowledgements

Code Institute - Learning from the code institute program were applied
W3 Schools - Used as a constant reference for code
