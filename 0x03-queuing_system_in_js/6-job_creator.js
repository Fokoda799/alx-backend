import kue from 'kue';
import redis from 'redis';

// Create a Redis client and Kue queue
const redisClient = redis.createClient();
const queue = kue.createQueue({ redis: redisClient });

// Create job data object
const jobData = {
  phoneNumber: '123-456-7890',
  message: 'Hello from Kue!'
};

// Create a new job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData)
  .on('enqueue', (id) => {
    console.log(`Notification job created: ${id}`);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', (errorMessage) => {
    console.error(`Notification job failed: ${errorMessage}`);
  })
  .save((err) => {
    if (err) {
      console.error('Error creating job:', err);
    }
  });
