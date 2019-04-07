# csv2text for saleae logic 

There are a number of ways to export data using the Saleae Logic [https://www.saleae.com/](https://www.saleae.com/). They have an article about it [here](https://support.saleae.com/user-guide/using-logic/saving-loading-and-exporting-data). 

The two programs provided will produce the text representation of the exported data, depending on how you have exported it. 

## saleae-csv2text

 The code will parse csv data in ASCII only format that is exported via Analyzers->Async Serial->Export as text/csv file 

##### File format: 

	Time [s],Value,Parity Error,Framing Error  
	0.062163420000000,b,, 

## saleae-csv2text-decoded-protocols
The code will parse csv data in ASCII only format that is exported via Decoded Protocols->Export search results 

##### File format: 

	Time [s], Analyzer Name, Decoded Protocol Result 
	0.062163420000000,Async Serial,b 

## Replacements: 
* The following replacements happen: 

		string.replace("' '",' ')
		string.replace('\\n','\n')
		string.replace('\\r','\r')
		string.replace('\\t','\t')
		string.replace('COMMA',',')
			
## Known issues: 
* Saleae Logic will export hex values as strings (e.g., '1' for 0x01) so keep this in mind if you find such items.


[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

