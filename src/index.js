import fs from 'fs-extra'
import generateOrder from './generator'
import sendOrder from './producer'

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
	sendOrder(order)
}

newOrders()
