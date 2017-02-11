// vrm.c
// PANDHASTAT RECEIVER
#define RELAY_ON LOW
#define RELAY_OFF HIGH

#include <VirtualWire.h>

unsigned long startts = 0 ; 

const int SECURITY_MS = 5*60*1000 ; // Will go down if no order after 5 minutes 
const int led_pin = 13;
const int transmit_pin = 9;
const int receive_pin = 12;
const int transmit_en_pin = 3;
const int relay_pin = 11 ;
int cc = 0 ;
void setup()
{
    delay(1000);
    Serial.begin(9600);	// Debugging only

    // Initialise the IO and ISR
    vw_set_tx_pin(transmit_pin);
    vw_set_rx_pin(receive_pin);
    vw_set_ptt_pin(transmit_en_pin);
    vw_set_ptt_inverted(true); // Required for DR3100
    vw_setup(1200);	 // Bits per sec

    vw_rx_start();       // Start the receiver PLL running
    pinMode(led_pin, OUTPUT);
    pinMode(relay_pin, OUTPUT) ; 
    digitalWrite(relay_pin, RELAY_OFF);

    Serial.println("PANDA TEMP ACTION READY");


}

void loop()
{

    uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN;
    unsigned long receivedat ; 
    if (vw_have_message()) {
      if (vw_get_message(buf, &buflen)) // Non-blocking
    
    {
	    int i;
      digitalWrite(led_pin, HIGH); // Flash a light to show received good message
	    // Message with a good checksum received, dump it.
	    Serial.print("Got: ");
      String message ;
    	for (i = 0; i < buflen; i++)
	    {
      message += (char)buf[i] ; 
	    Serial.print((char)buf[i], HEX);
	    Serial.print(' ');
	    }
	    Serial.println();
      digitalWrite(led_pin, LOW);

      Serial.println(message) ; 
     
      if  (message == "PF")  
        { 
          Serial.println("CALL FOR ACTION : OFF") ; 
          digitalWrite(relay_pin, RELAY_OFF);
          startts = millis() ; 
        }
        if (message == "PO")  
        { 
          Serial.println("CALL FOR ACTION : ON") ; 
          digitalWrite(relay_pin, RELAY_ON);
          startts = millis() ; 
        }  
      } else {
          Serial.println("CORRUPTED") ; 
      }
      
    }

      unsigned long dlm = millis()-startts; 

      if (dlm > SECURITY_MS) {
        //  Serial.print("SECURITY : CALL FOR ACTION OFF") ; 
          digitalWrite(relay_pin, RELAY_OFF);
          startts = millis() ; 
      }
      
  
}
