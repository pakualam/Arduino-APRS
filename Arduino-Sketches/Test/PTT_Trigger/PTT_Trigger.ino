#define PTT 7

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // connect serial 
  Serial.println("Starting Up PTT Trigger Test"); 
  pinMode(PTT, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(PTT, HIGH);
  Serial.println("PTT On");
  delay(2000);
  digitalWrite(PTT, LOW);
  Serial.println("PTT Off");
  delay(5000);
}
