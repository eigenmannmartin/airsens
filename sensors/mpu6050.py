from I2C import I2C


class MPU6050():
	MPU6050_ADRESS = 0x68
	MPU6050_RA_GYRO_CONFIG = 0x1B
	MPU6050_GYRO_FS_250 = 0x00
	MPU6050_RA_ACCEL_CONFIG = 0x1C
	MPU6050_ACCEL_FS_2 = 0x00
	MPU6050_RA_PWR_MGMT_1 = 0x6B
	MPU6050_PWR1_ON_BIT = 0

	MPU6050_RA_WHO_AM_I = 0x75
	MPU6050_RA_ACCEL_XOUT_H = 0x3B

	def __init__(self, busnum=-1, debug=False):
		self.accel = I2C(self.MPU6050_ADRESS, busnum, debug)

		self.accel.write8(self.MPU6050_RA_GYRO_CONFIG, self.MPU6050_GYRO_FS_250)
		self.accel.write8(self.MPU6050_RA_ACCEL_CONFIG, self.MPU6050_ACCEL_FS_2)

		self.accel.write8(self.MPU6050_RA_PWR_MGMT_1, self.MPU6050_PWR1_ON_BIT)
	def getData(self):
		print self.accel.readList(self.MPU6050_RA_ACCEL_XOUT_H,6)

			
	def testConnection(self):
		if self.accel.readS8(self.MPU6050_RA_WHO_AM_I) == int(0x68):
			print "Everything went perfect"
			return True
		return False



if __name__ == '__main__':
	accel = MPU6050()
	accel.testConnection()
	accel.getData()

