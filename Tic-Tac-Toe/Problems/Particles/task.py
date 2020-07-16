spin = input()
charge = input()
particle = ''
if spin == '1/2':
	if charge == '-1/3':
		particle = 'Strange Quark'
	elif charge == '2/3':
		particle = 'Charm Quark'
	elif charge == '-1':
		particle = 'Electron Lepton'
	elif charge == '0':
		particle = 'Muon Lepton'
elif spin == '1':
	particle = 'Photon Boson'
	
print(particle)
