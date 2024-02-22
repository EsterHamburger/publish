const amqp = require('amqplib');
require('dotenv').config();
const rabbitMQ_connection = process.env.RABBITMQ_CONNECTION;

let connection = null;
let channel;

const initConnection = async () => {
    try {
        if (!connection) {
            connection = await amqp.connect(rabbitMQ_connection);
        }
    } catch {
        throw new Error('Failed to connect to rabbitmq');
    }
};

const createChannel = async () => {
    try {
        if (!connection) {
            throw new Error('No connection to rabbitMQ');
        }
        if (!channel) {
            channel = await connection.createConfirmChannel();
        }
        return channel;
    } catch {
        throw new Error('Failed to create channel');
    }
};

module.exports = { initConnection, createChannel };