#define NUM_SAMPLES 16

long timestamp;
// circular buffers used to storing past samples for moving average
float oilPres[NUM_SAMPLES + 1] = {0}, coolant[NUM_SAMPLES + 1] = {0};
// current index in the circular buffers
int idx = 0;
char buf[64];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  timestamp = millis();
  // store new values
  oilPres[idx] = random(1000) / 10.0; // 0.0 to 100.0
  coolant[idx] = 70 + (random(400) / 10.0); // 70.0 to 110.0
  
  // increment idx and loop it around if it passes end of buffer
  if(++idx >= NUM_SAMPLES) idx = 0;
  // sum up all values into next index and divide by number of samples to get average
  for(int i = 0; i < NUM_SAMPLES; i++) {
    if(i != idx) {
      oilPres[idx] += oilPres[i];
      coolant[idx] += coolant[i];
    }
  }
  oilPres[idx] /= NUM_SAMPLES;
  oilPres[idx] /= NUM_SAMPLES;

  // "ts,oilPres,coolant\t"  
  Serial.print(timestamp);
  Serial.print(",");
  Serial.print(oilPres[idx], 1);
  Serial.print(",");
  Serial.println(coolant[idx], 1);
  delay(10);
}
