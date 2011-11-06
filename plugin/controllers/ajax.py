##############################################################################
#                        2011 E2OpenPlugins                                  #
#                                                                            #
#  This file is open source software; you can redistribute it and/or modify  #
#     it under the terms of the GNU General Public License version 2 as      #
#               published by the Free Software Foundation.                   #
#                                                                            #
##############################################################################

from models.services import getCurrentService, getBouquets, getChannels, getSatellites, getProviders
from base import BaseController

class AjaxController(BaseController):
	def __init__(self, session, path = ""):
		BaseController.__init__(self, path)
		self.session = session
		
	def P_current(self, request):
		return getCurrentService(self.session)
		
	def P_bouquets(self, request):
		if "id" in request.args.keys():
			bouquets = getBouquets(request.args["id"][0])
		else:
			bouquets = getBouquets()
		return bouquets
		
	def P_providers(self, request):
		if "id" in request.args.keys():
			providers = getProviders(request.args["id"][0])
		else:
			providers = getProviders()
		return providers
		
	def P_satellites(self, request):
		return getSatellites()
	
		
	def P_channels(self, request):
		if "id" in request.args.keys():
			channels = getChannels(request.args["id"][0])
		else:
			channels = getChannels()
		return channels
		
