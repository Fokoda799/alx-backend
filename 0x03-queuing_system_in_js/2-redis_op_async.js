import redis from 'redis';
import {promisify} from 'util'

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const getAsync = promisify(client.get).bind(client)

const displaySchoolValue = async (schoolName) => {
  try {
    const replay = await getAsync(schoolName)
    console.log(replay)
  } catch (err) {
    console.log(`Error retrieving value: ${err.message}`)
  }
};

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
