import kue from 'kue';

// Create a queue using Kue
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send a notification
function sendNotification(phoneNumber, message, job, done) {
    // Track the job progress at the start
    job.progress(0, 100);

    // Check if the phone number is blacklisted
    if (blacklistedNumbers.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // Simulate progress to 50%
    job.progress(50, 100);

    // Log the notification being sent
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // Simulate job completion
    done();
}

// Process jobs in the queue named 'push_notification_code_2', with a concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});

// Event listeners for job status updates
queue.on('job complete', function(id, result) {
    kue.Job.get(id, function(err, job) {
        if (err) return;
        job.remove(function(err) {
            if (err) throw err;
            console.log(`Notification job #${job.id} completed`);
        });
    });
});

queue.on('job failed', function(id, errorMessage) {
    console.log(`Notification job #${id} failed: ${errorMessage}`);
});

queue.on('job progress', function(id, progress) {
    console.log(`Notification job #${id} ${progress}% complete`);
});
