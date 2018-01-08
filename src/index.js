import fs from 'fs-extra'
import { createLogger, format, transports } from 'winston'
import generateOrder from './generator'
import sendOrder from './producer'

const { combine, timestamp, label, printf } = format

const loggerFormat = printf(info => {
	return `${info.timestamp} [${info.level}]: ${info.message}`
})

const logger = createLogger({
	format: combine(timestamp(), loggerFormat),
	transports: [
		new transports.Console(),
		new transports.File({ filename: 'orders.log' }),
	],
})

const newOrders = async () => {
	const hives = await fs.readJson(`${__dirname}/files/hives.json`)
	setInterval(() => {
		newOrder(hives)
	}, 1000)
}

const newOrder = hives => {
	const { from, to } = generateOrder(hives)
	const order = {
		from: from.id,
		to: to.id,
	}
	logger.info(`new order { from: ${order.from}, to: ${order.to} }`)
	sendOrder(order)
}

newOrders()
