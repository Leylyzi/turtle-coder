function main() {
	turtle->setSpeed(1000)
	turtle->forward(40)
	turtle->rightTurn(90)
	turtle->forward(40)
	turtle->rightTurn(90)
	turtle->forward(40)
	turtle->rightTurn(180)
	turtle->forward(40)
	turtle->rightTurn(90)
	turtle->back(20)
	drawcircle(2)
	drawQuartercircle(1)
	turtle->back(100)
	turtle->penUp()
	turtle->leftTurn(90)
	turtle->forward(10)
	turtle->rightTurn(90)
	turtle->penDown()
	turtle->forward(70)
	turtle->leftTurn(90)
	turtle->penUp()
	turtle->forward(10)
	turtle->rightTurn(90)
	turtle->penUp()
	turtle->rightTurn(180)
	turtle->forward(15)
	turtle->penDown()
	turtle->forward(50)
	turtle->back(50)
	turtle->penUp()
	turtle->rightTurn(90)
	turtle->forward(70)
	turtle->penDown()
	turtle->leftTurn(90)
	turtle->forward(50)
	turtle->back(50)
	turtle->penUp()
	turtle->rightTurn(90)
	turtle->forward(10)
	turtle->rightTurn(90)
	turtle->penDown()
	turtle->forward(10)
	turtle->leftTurn(180)
	turtle->forward(70)
	turtle->penUp()
	turtle->rightTurn(90)
	turtle->forward(10)
	turtle->penDown()
	turtle->rightTurn(90)
	turtle->forward(100)
	turtle->penUp()
	turtle->forward(10)
	turtle->rightTurn(45)
	turtle->forward(20)
	turtle->rightTurn(45)
	turtle->penDown()
	turtle->forward(20)
	turtle->penUp()
	turtle->forward(30)
	turtle->penDown()
	turtle->forward(20)
	turtle->penUp()
	turtle->forward(10)
	turtle->back(10)
	turtle->rightTurn(90)
	turtle->forward(50)
	drawhalfcircle(mod(2,2))
}
function drawcircle() {
	for(var i < 360) {
		turtle->forward(1)
		turtle->leftTurn(1)
	}

}
function drawquartercircle() {
	for(var m < 90) {
		turtle->forward(1)
		turtle->rightTurn(1)
	}

}
function drawQuartercircle() {
	for(var j < 90) {
		turtle->forward(1)
		turtle->leftTurn(1)
	}

}
function drawEighthcircle() {
	for(var l < 90) {
		turtle->forward(1)
		turtle->rightTurn(1)
	}

}
function drawHalfcircle() {
	for(var k < 180) {
		turtle->forward(1)
		turtle->leftTurn(1)
	}

}
function drawhalfcircle() {
	for(var n < 180) {
		turtle->forward(1)
		turtle->rightTurn(1)
	}

}
