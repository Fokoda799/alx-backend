import kue from 'kue';

function createPushNotificationsJobs(jobs, queue) {
    // Check if jobs is an array
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    // Loop through the jobs array
    jobs.forEach((jobData) => {
        // Create a new job in the queue push_notification_code_3
        const job = queue.create('push_notification_code_3', jobData)
            .save((err) => {
                if (!err) {
                    console.log(`Notification job created: ${job.id}`);
                }
            });

        // Event listener for job completion
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });

        // Event listener for job failure
        job.on('failed', (errorMessage) => {
            console.log(`Notification job ${job.id} failed: ${errorMessage}`);
        });

        // Event listener for job progress
        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    });
}

export default createPushNotificationsJobs;
