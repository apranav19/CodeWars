'''
	Similar to activity scheduling problem
	@author - Pranav Angara
'''

class SongScheduler:
	def __init__(self):
		self.duration_tone = None


	def max_songs(self, duration, tone, time):
		self.build_duration_map(duration, tone)
		duration.sort()
		
		current = songs = 0

		for i in xrange(len(duration)-1):
			if current + duration[i] > time:
				return songs

			songs += 1

			curr_tone = self.duration_tone[duration[i]].pop()
			next_tone = self.duration_tone[duration[i+1]][len(self.duration_tone[duration[i+1]])-1]

			diff = abs(curr_tone - next_tone)
			current += (duration[i] + diff)

		if current + duration[i] <= time:
			songs += 1

		return songs

	def build_duration_map(self, duration, tone):
		self.duration_tone = {}

		for i,j in zip(duration, tone):
			if i in self.duration_tone:
				self.duration_tone[i].append(j)
			else:
				self.duration_tone[i] = [j]
