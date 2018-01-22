import wx
import time

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,
					'Hikcentral1.x Simulate Client',
					size=(800,480))

		panel = wx.Panel(self)	
		panel.SetBackgroundColour('#aaaaaa')

		#登陆登出按钮
		self.btnLogin = wx.Button(panel,-1,"Login",size = (75,25))
		self.btnLogout = wx.Button(panel,-1,"Logout",size = (75,25))
		#绑定登陆登出操作
		self.Bind(wx.EVT_BUTTON,self.OnButtonLogin,self.btnLogin)
		self.Bind(wx.EVT_BUTTON,self.OnButtonLogout,self.btnLogout)


		#发送清空按钮
		self.btnSent = wx.Button(panel,-1,"Sent",size = (75,25))
		self.btnClear = wx.Button(panel,-1,"Clear",size = (75,25))
		#绑定发送和清空操作
		self.Bind(wx.EVT_BUTTON,self.OnButtonSent,self.btnSent)
		self.Bind(wx.EVT_BUTTON,self.OnButtonClear,self.btnClear)


		#设置发送请求输入框
		labelUrl = wx.StaticText(panel,-1,"Request URL")
		self.textURL = wx.TextCtrl(panel,-1,size = (50,25),
							style = wx.TE_MULTILINE)

		labelMethod = wx.StaticText(panel,-1,"Request Method")
		self.textMethod = wx.TextCtrl(panel,-1,size = (50,25),
							style = wx.TE_MULTILINE)

		labelQuery = wx.StaticText(panel,-1,"Request Query")
		self.textQuery = wx.TextCtrl(panel,-1,size = (50,25),
							style = wx.TE_MULTILINE)


		#响应数据输出框
		labelAll = wx.StaticText(panel,-1,"Resopnd Message")
		self.textAll = wx.TextCtrl(panel,-1,size = (480,200),
							style = wx.TE_MULTILINE|wx.TE_READONLY)
		#请求数据输入框
		lableIn = wx.StaticText(panel,-1,"Request XML")
		self.textIn = wx.TextCtrl(panel,-1,size = (480,100),
							style = wx.TE_MULTILINE)

		#自动布局
		btnSizer_log = wx.BoxSizer()
		btnSizer_log.Add(self.btnLogin,proportion=0)
		btnSizer_log.Add(self.btnLogout,proportion=0)


		btnSizer = wx.BoxSizer()
		btnSizer.Add(self.btnSent,proportion=0)
		btnSizer.Add(self.btnClear,proportion=0)

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(btnSizer_log,proportion=0,flag = wx.ALIGN_CENTER)

		mainSizer.Add(labelUrl,proportion=0,flag = wx.ALIGN_CENTER)
		mainSizer.Add(self.textURL,proportion=0,flag = wx.EXPAND)
		mainSizer.Add(labelMethod,proportion=0,flag = wx.ALIGN_CENTER)
		mainSizer.Add(self.textMethod,proportion=0,flag = wx.EXPAND)
		mainSizer.Add(labelQuery,proportion=0,flag = wx.ALIGN_CENTER)
		mainSizer.Add(self.textQuery,proportion=0,flag = wx.EXPAND)

		mainSizer.Add(lableIn,proportion=0,flag = wx.ALIGN_CENTER)
		mainSizer.Add(self.textIn,proportion=0,flag = wx.EXPAND)

		mainSizer.Add(labelAll,proportion=0,flag = wx.ALIGN_CENTER)
		mainSizer.Add(self.textAll,proportion=1,flag = wx.EXPAND)
		mainSizer.Add(btnSizer,proportion=0,flag = wx.ALIGN_CENTER)


		panel.SetSizer(mainSizer)

	def OnButtonSent(self,event):
		userInput = self.textIn.GetValue()
		self.textIn.Clear()
		now = time.ctime()
		inMsg = " you(%s):\n%s \n" % (now,userInput)

		self.textAll.AppendText(inMsg)

	def OnButtonClear(self,event):
		self.textAll.Clear()


	def OnButtonLogin(self,event):
		self.textAll.AppendText('login success!\n')

	def OnButtonLogout(self,event):
		self.textAll.AppendText('logout success!\n')

		
if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()

