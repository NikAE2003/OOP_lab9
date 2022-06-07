main = """
*{
	color: #ddd;
	font: 75 12pt "Century Gothic";
	Background-color: #444;
	border: none
}

QPushButton{
	background-color: #56c;
	border-radius: 5;
}

QPushButton::pressed{
	background-color: #333;
	color: #56c;
	border: 2px solid #56c;
	border-radius:5;
}

QLineEdit, QSpinBox{
	border-bottom:2px solid #56c;
}
"""

tableHeader = """
*{
	background-color: transparent;
	border: None;
}

QLabel{
	background-color: #444;
}
"""

tableItem = """
*{
	background-color: transparent;
	border: None;
}

QLabel{
	background-color: #333;
}
"""

tableItem_selected = """
*{
	background-color: transparent;
	border: None;
}

QLabel{
	background-color: #56c;
}
"""