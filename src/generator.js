const generateOrder = hives => {
	const fromLength = hives.length
	const from = Math.floor(Math.random() * (fromLength - 1))

	const fromHive = hives[from]

	const possibleHives = hives.filter(hive => hive.id !== fromHive.id)
	const toLength = possibleHives.length
	const to = Math.floor(Math.random() * (toLength - 1))

	const toHive = possibleHives[to]

	return {
		from: fromHive,
		to: toHive,
	}
}

export default generateOrder
