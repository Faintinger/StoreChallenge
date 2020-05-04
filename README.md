# StoreChallenge
 Small Store Simulaton base on text DB

By: Omar Garcia
	GitHub Faintinger

Purpose:
		Create an small API to calculate: 
			- The total number of items sold on that day.
			- The total number of customers that made an order that day.
			- The total amount of discount given that day.
			- The average discount rate applied to the items sold that day.
			- The average order total for that day
			- The total amount of commissions generated that day.
			- The average amount of commissions per order for that day.
			- The total amount of commissions earned per promotion that day.

		Files required: 
			- orders
			- order_lines
			- products
			- product_promotions
			- promotions
			- commissions

		How to Use:
			0. Download the project and paste in your local drive
			1. Install python 3.X and all dependencies from requirements.txt
			2. Open config.properties and fill with all the locations of the files
			3. Open StoreChallenge.py and Run it.
			4. By default the app is set to port 8080, Open your web browser on:
				localhost:8080/DateReport?date=<date in format yyyy-mm-dd>
			
			Additional functionalities
			/HelloWorld --> Return a Json with a HelloWorld.
			/ReloadDAta --> Triggers the app to reload the files if a change is made.

		Error Handling
			If the date format is wrong it will return a msg error "This is not a valid date format"
			Also if the files are bad structured the end point will not receive a different error
			But the stacktrace will be displayed on the console.

			This is just basic error handling. Improvements can be done on further iterations

		Future Improvements:

			- Security implementation
			- Advance error handling
			- Moving out of just cache DB
				- if the Text files are too big to load on memory implement a DB conection to load into dataframes