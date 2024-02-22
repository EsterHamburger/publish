const { StatusCodes } = require('http-status-codes');
const { initConnection, createChannel } = require('./rabbitMQConnection');
const queue_name = process.env.QUEUE_NAME;
require('dotenv').config();

const addMessageToQueue = async (message) => {
    const messageOptions = {
        content: Buffer.from(JSON.stringify(message))
    };

    try {
        await initConnection();
        const channel = await createChannel();

        await channel.assertQueue(queue_name);
        channel.sendToQueue(queue_name, messageOptions.content, {
            headers: messageOptions.options.headers
        });
        await channel.waitForConfirms();
        return StatusCodes.OK;
    } catch (error) {
        const asError = error;
        throw new Error(asError?.message);
    }
};

module.exports = { addMessageToQueue };