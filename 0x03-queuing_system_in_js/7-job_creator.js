import kue from 'kue';
import redis from 'redis';

// Create a Redis client and Kue queue
const redisClient = redis.createClient();
const queue = kue.createQueue({ redis: redisClient });

// Array of job data
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// Loop through the jobs array and create a job for each object
jobs.forEach((jobData, index) => {
  const job = queue.create('push_notification_code_2', jobData)
    .on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    })
    .on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    })
    .on('failed', (errorMessage) => {
      console.error(`Notification job ${job.id} failed: ${errorMessage}`);
    })
    .on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    })
    .save((err) => {
      if (err) {
        console.error('Error creating job:', err);
      }
    });
});
