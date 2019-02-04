
const int temperaturePin = 0;
void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);
}

void loop() {
  
  int lectura = analogRead(0);
  float voltaje = 5.0 /1024 * lectura ; 
  float temp = voltaje * 100 -50 ; 
  Serial.println(temp) ; 
  delay(5000);

}

float getVoltage(int pin)
{  
   
  return (analogRead(pin) * 0.004882814);
  
}
