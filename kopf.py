function main() {
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
	turtle->setPenColor(red)
	# begin left hair
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
	# end left hair
	turtle->setPenColor(black)
	turtle->penUp()
	turtle->rightTurn(90)
	turtle->forward(70)
	turtle->penDown()
	turtle->leftTurn(90)
	turtle->setPenColor(red)
	# begin right hair
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
	# end right hair
	turtle->setPenColor(black)
	turtle->penUp()
	turtle->forward(10)
	turtle->rightTurn(45)
	turtle->forward(20)
	turtle->rightTurn(45)
	turtle->penDown()
	turtle->setPenColor(blue)
	# begin eyes
	turtle->forward(20)
	turtle->penUp()
	turtle->forward(30)
	turtle->penDown()
	turtle->forward(20)
	# end eyes
	turtle->setPenColor(black)
	turtle->penUp()
	turtle->forward(10)
	turtle->back(10)
	turtle->rightTurn(90)
	turtle->forward(50)
	turtle->setPenColor(orange)
	# begin mouth
	turtle->rightTurn(180)
	turtle->back(10)
	turtle->penDown()
	turtle->forward(10)
	turtle->back(5)
	turtle->leftTurn(90)
	turtle->forward(60)
	turtle->rightTurn(90)
	turtle->forward(5)
	turtle->back(10)
	# end mouth
	turtle->setPenColor(black)
	turtle->penUp()
	turtle->forward(90)
	turtle->penDown()
	turtle->setPenColor(red)
	# begin bangs
	turtle->back(20)
	turtle->penUp()
	turtle->rightTurn(90)
	turtle->forward(20)
	turtle->leftTurn(90)
	turtle->penDown()
	turtle->forward(30)
	turtle->penUp()
	turtle->rightTurn(180)
	turtle->forward(30)
	# end bangs
	turtle->rightTurn(90)
	turtle->penDown()
	turtle->forward(30)
	turtle->penUp()
	turtle->forward(200)
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
function drawHalfcircle() {
	for(var k < 180) {
		turtle->forward(1)
		turtle->leftTurn(1)
	}

}
function farbwechsel(brown) {
	turtle->setPenColor(brown)

}
