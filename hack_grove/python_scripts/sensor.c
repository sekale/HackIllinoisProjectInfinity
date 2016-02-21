#include <unistd.h>
#include <signal.h>
#include <iostream>
#include "mma7660.h"

using namespace std;

int shouldRun = true;

void sig_handler(int signo)
{
  if (signo == SIGINT)
    shouldRun = false;
}

int main(int argc, char **argv)
{
  signal(SIGINT, sig_handler);

//! [Interesting]
  // Instantiate an MMA7660 on I2C bus 0

  upm::MMA7660 *accel = new upm::MMA7660(MMA7660_I2C_BUS, 
                                         MMA7660_DEFAULT_I2C_ADDR);

  // place device in standby mode so we can write registers
  accel->setModeStandby();

  // enable 64 samples per second
  accel->setSampleRate(upm::MMA7660::AUTOSLEEP_64);
  
  // place device into active mode
  accel->setModeActive();

  while (shouldRun)
    {
      int x, y, z;
      
      accel->getRawValues(&x, &y, &z);
      cout << "Raw values: x = " << x 
           << " y = " << y
           << " z = " << z
           << endl;
      
      float ax, ay, az;
      
      accel->getAcceleration(&ax, &ay, &az);
      cout << "Acceleration: x = " << ax 
           << "g y = " << ay
           << "g z = " << az
           << "g" << endl;
      
      usleep(500000);
    }

//! [Interesting]

  cout << "Exiting..." << endl;

  delete accel;
  return 0;
}