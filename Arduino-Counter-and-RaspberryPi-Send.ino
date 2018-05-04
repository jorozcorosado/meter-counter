const byte interruptPin = 2;
volatile int counter = 0;
int lastcount=0;
char dataString[50] = {0};
int a =0; 

void setup() {
  pinMode(interruptPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin), counterfun, CHANGE);
  Serial.begin(9600);
  
}

void loop() {
  if(lastcount!=counter){
  sprintf(dataString,"%02X", counter);
  Serial.println(dataString);
  delay(100);
  }
  lastcount = counter;

}

void counterfun() {
counter+=1;

}
