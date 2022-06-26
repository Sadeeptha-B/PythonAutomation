# XPath - xml path language
# Query language for selecting nodes from an xml document

# // - Pick matching node located at any level
# //tagName[1]: Indexed from 1, //tagName[@AttributeName="Value"]
# XPath functions - contains(), starts-with(): tagName[contains(@AttributeName,"Value")]
# tagName[() and/or ()]
# //article/div:- / to select the children from the node set on the left side of this character
# //h1/text(), //article//text
# //h1/.., ./*, @- Select attribute
