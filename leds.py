def map_led_ids(led_ids):
	registers = [0, 0, 0, 0]
	for led in led_ids:
		nled = led - 1
		id = nled // 32
		element = nled % 32
		value = 2**element
		registers[id] += value
	ids = []
	for i in range(4):
		ids += ['.id{} = {}'.format(i, registers[i])]
	return ids


def map_leds(layer_lst):
	for layer in range(len(layer_lst)):
		for group in layer_lst[layer]:
			flags = ["LED_FLAG_MATCH_LAYER", "LED_FLAG_MATCH_ID"]
			ids = map_led_ids(group[-1])
			layers = ['.layer = {}'.format(layer)]
			finals = []
			if (group[0] == "rgb"):
				flags += ["LED_FLAG_USE_RGB"]
				for i in range(3):
					finals += ['.{} = {}'.format(group[0][i], group[1][i])]
			if (group[0] == "hex"):
				flags += ["LED_FLAG_USE_RGB"]
				for i in range(3):
					finals += [
					    '.{} = {}'.format(
					        "rgb" [i],
					        int("0x" + group[1][2 * i + 1:2 * i + 3], 16))
					]
			if (group[0] == "pat"):
				flags += ["LED_FLAG_USE_PATTERN"]
				finals += ['.pattern = {}'.format(group[1])]
			if (group[0] == "rot"):
				flags += ["LED_FLAG_USE_ROTATE_PATTERN"]
			res = '{{ .flags = {}, {} }}'.format(
			    ' | '.join(flags), ', '.join(layers + ids + finals))
			print(res)


def main():
	dark_gray = [
	    6, 7, 8, 9, 14, 15, 16, 30, 31, 32, 33, 34, 48, 49, 50, 51, 63, 64, 75,
	    76, 77, 78, 79, 81, 82, 83, 84, 85, 86, 87
	]
	light_gray = [
	    2, 3, 4, 5, 10, 11, 12, 13, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
	    28, 29, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 52, 53, 54,
	    55, 56, 57, 58, 59, 60, 61, 62, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
	    80
	]
	back_light = range(88, 120)

	bigass = [[["rgb", [33, 33, 33], dark_gray], ["hex", "#ffcc00", dark_gray],
	           ["rgb", [66, 66, 66], light_gray], ["rot", back_light]]]

	map_leds(bigass)

main()
