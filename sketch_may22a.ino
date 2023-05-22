int switchState = 0;

// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(11,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  switchState = digitalRead(2); 

  if (switchState == LOW)
  // Wenn Schalter nicht gedrückt
 {  digitalWrite(11, LOW);
    digitalWrite(12, LOW);
    digitalWrite(13, LOW);     
    digitalWrite(8, LOW);
    digitalWrite(7, LOW);
  
  } else {
    // Wenn schakter gedrückt
    digitalWrite(11, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(13, HIGH);
    digitalWrite(8, LOW);
    digitalWrite(7, HIGH);
    
    delay(50);

    digitalWrite(11, LOW);
    digitalWrite(12, LOW);
    digitalWrite(13, LOW);
    digitalWrite(8, HIGH);
    digitalWrite(7, LOW);
    
    delay(50);
  }
}
