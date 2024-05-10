<h1>Welcome to my trading bot project</h1>

<h3>Idea</h3>
 My bot use 2 Ema line to indicate when to place order.The first is called Ema fast and the second one is called Ema slow,which mean that index of the first is smaller than the second.
<p>
	<br>While trading,the Ema fast is represent for the price trend in short term,Ema slow represent for the medium term.<br>
	<br>&nbsp If the 'short' line cut the 'medium' line from under,we will say that the 'cross-over' event happen which mean in short term,the price is going to rise.We will place Long order in the open price of next candle.<br>
	<br>&nbsp In constrast,if the Ema fast cut the Ema slow from top to bottom,that is when the 'cross-under' event occur which mean the price can go down in short term and we will place Sell order on the next candle.<br>
	<br>That's how the algorithm work,let's dive into the project now.
</p>

<h2>Code</h2>
<p>
	In this project,there are 4 main part the corresponding to 4 big folders you can see when you clone this repo order by it's important:
	<ol>
		<li>Trading</li>
		<li>Database</li>
		<li>Chart</li>
		<li>Report</li>
		<li>Setup</li>
	</ol>
	*Note:In the whole project,folder will be named capitalize,important file will be named in lowercase and,function file will be named in uppercase.
</p>
<h3>1/Trading</h3>
<p>
	This is the most important folder in the whole project,it gather data,send to database,check condition and place orders,etc...
	<ul>
		<li>
			<b>Test folder:</b> &nbsp use testing small features that don't need to create a new branch.
		</li>
		<li>
			<b>.env:</b> &nbsp use for set the api/secret key.
		</li>
		<li>
			<b>data.py:</b> &nbsp use for gather raw data from binance,calculate ema values and store them in database.
		</li>
		<li>
			<b>ERROR.py/ERROR.log:</b> &nbsp the ERROR.py will send an alert email for user and write it to the ERROR.log to retrieve in future.
		</li>
		<li>
			<b>fake_data.py:</b> &nbsp can generate some fake data,store to database quickly to test and track workflow of project.
		</li>
		<li>
			<b>FILLING_DATA.py:</b> &nbsp use for filling some first data before running the bot to prevent big deviation.
		</li>
		<li>
			<b>FUNCTIONAL.py:</b> &nbsp store some usefull function that can be used in the whole project.
		</li>
		<li>
			<b>IMPORT.py:</b> &nbsp use for import all needed library.
		</li>
		<li>
			<b>INDICATOR.py:</b> &nbsp use to calculate the new Ema values.
		</li>
		<li>
			<b>PARAMETER.py:</b> &nbsp store some global variable.
		</li>
		<li>
			<b>ping_process.py:</b> &nbsp check runnning applications to make sure no part of the project suddenly crash without any alert.
		</li>
		<li>
			<b>trade.py:</b> &nbsp check if cross over/under happened to place order.
		</li>
	</ul>
</p>

<h3>2/Database</h3>
<p>
	In this project,we use sqlite database to store and process data.The Database folder is where the database placed and if contain some function to interact with the database.<br>
	<p>
		Before go deeper into folder,let's talk a little about the structure of the database:
		<ul>
			<li>
				<b>Ema:</b> &nbsp this table store the ema value from index 1-100 and can store multiple timeframe that can indicate by the timeframe colume.
			</li>
			<li>
				<b>Price:</b> &nbsp store the normal Open,High,Low,Close,Volume and timeframe of current assert.
			</li>
			<li>
				<b>History:</b>&nbsp store all tracsations that has been made since the bot started.
			</li>
			<li>
				<b>Open_orders:</b> &nbsp store all information about current opening orders.
			</li>
			<b>Trigger:</b> &nbsp check that all Ema,Price table don't exceed 120 rows.
		</ul>
	</p>
	<ul>
		<li>
			<b>DB_FUNCTION.py:</b> &nbsp create 3 function(insert,query,delete) for more easy to handle with database.
		</li>
		<li>
			<b>ddl.py:</b> &nbsp store the ddl string to create all required table,trigger.
		</li>
		<li>
			<b>dml.py:</b> &nbsp use for manually query,update data if something happen.
		</li>
		<li>
			<b>GENERATE_DDL.py:</b> &nbsp use for generate ddl faster,also like a reserve for ddl.py if the ddl.py was erased somewhere.
		</li>
	</ul>
</p>
<h3>3/Chart</h3>
<p>
	The Chart folder can visualize some normal candlestick chart,ema line in terminal for easier to make sure everything work fine,also don't need to go to binance to check all. 
	<ul>
		<li>
			<b>main.py:</b> &nbsp read data from the database and draw it on terminal.
			<b>test.py:</b> &nbsp use to test some feature,chart to draw on main.py
		</li>
	</ul>
</p>

<h3>4/Report</h3>
<p>
	Report folder summarize and give some usefull information profit/loss of the bot.
	<ul>
		<li>
			<b>main.py:</b> &nbsp get data from History table of the database,calculate PnL,Roi,tracking run time and the growth chart of the project.
		</li>
	</ul>
</p>
<h3>5/Setup</h3>
<p>
	Setup is not the folder,but contain all the files that outside of 4 folders that listed above.<br>
	The project use GNU screen package to run all the process asynchronously.
	<ul>
		<li>
			<b>HYPERPARAMETER.py:</b> &nbsp This is where you setup the parameter for the bot about how much,what assert you want to trade,etc...
		</li>
		<li>
			<b>start_trade.sh:</b> &nbsp set the workflow and run the FILLING_DATA.py to prepare data,and check for valid HYPERPARAMETER before trade to prevent bugs.
		</li>
		<li>
			<b>.trade_setup.py</b> &nbsp get the information of HYPERPARAMETER to write the config screen architecture to .trade_setup for GNU screen package.
		</li>
		<li>
			<b>requirements.txt:</b> &nbsp list all required python library,linux package for the bot to run.
		</li>
	</ul>
</p>
