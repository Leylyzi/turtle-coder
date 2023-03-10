function main() {
	turtle->setPenSize(9)
	turtle->setSpeed(1000)
	turtle->setPenColor(yellow)
	drawCircle()
	turtle->rightTurn(90)
	turtle->forward(20)
	turtle->setPenColor(black)
	drawCircle()
	turtle->rightTurn(90)
	turtle->setPenColor(green)
	drawCircle()
	turtle->leftTurn(90)
	turtle->forward(140)
	turtle->setPenColor(red)
	drawCircle()
	turtle->rightTurn(180)
	turtle->forward(225)
	turtle->rightTurn(90)
	turtle->forward(55)
	turtle->setPenColor(blue)
	drawCircle()
}
function drawCircle() {
	turtle->penDown()
	for(var i < 360) {
		turtle->forward(1)
		turtle->leftTurn(1)
	}
	turtle->penUp()
}
