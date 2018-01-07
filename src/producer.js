import path from 'path'
import jackrabbit from 'jackrabbit'

require('dotenv').config({ path: path.join(process.env.PWD, '.env') })

const rabbit = jackrabbit(process.env.CLOUDAMQP_URL)
const exchange = rabbit.default()

const sendOrder = order => {
	exchange.publish(order, { key: process.env.PRODUCER_QUEUE })
}

export default sendOrder
