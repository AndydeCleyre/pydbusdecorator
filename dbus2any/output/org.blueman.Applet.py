'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /
* org.blueman.Applet
* 

'''
from pydbusdecorator import DbusInterface, DbusMethod, DbusSignal, DbusAttr
        
class Applet(object):
    '''
    Applet
    
    Usage:
    ------
    
    >> myApplet = Applet()
    since this you can access any method, attribute or signal defined below this.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myApplet.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myApplet.bar
    >>> myApplet.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myApplet.spam = lambda eggs: do_something(eggs)
    
    '''
	@DbusInterface("org.blueman.Applet", "/", "org.blueman.Applet")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def RefreshServices(self, arg_path, *arg, **kw):
		"""
		RefreshServices method:
		
		Parameters
		----------
		path: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def CancelDeviceCreation(self, arg_adapter_path, arg_address, *arg, **kw):
		"""
		CancelDeviceCreation method:
		
		Parameters
		----------
		adapter_path: s, direction: in,
		address: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def SetPluginConfig(self, arg_plugin, arg_value, *arg, **kw):
		"""
		SetPluginConfig method:
		
		Parameters
		----------
		plugin: s, direction: in,
		value: b, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def CreateDevice(self, arg_adapter_path, arg_address, arg_pair, arg_time, *arg, **kw):
		"""
		CreateDevice method:
		
		Parameters
		----------
		adapter_path: s, direction: in,
		address: s, direction: in,
		pair: b, direction: in,
		time: u, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def QueryAvailablePlugins(self, *arg, **kw):
		"""
		QueryAvailablePlugins method:
		
		Parameters
		----------
		
		    arg1: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def TransferControl(self, arg_pattern, arg_action, *arg, **kw):
		"""
		TransferControl method:
		
		Parameters
		----------
		pattern: s, direction: in,
		action: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def GetBluetoothStatus(self, *arg, **kw):
		"""
		GetBluetoothStatus method:
		
		Parameters
		----------
		
		    arg1: b, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def ServiceProxy(self, arg_interface, arg_object_path, arg__method, arg_args, *arg, **kw):
		"""
		ServiceProxy method:
		
		Parameters
		----------
		interface: s, direction: in,
		object_path: o, direction: in,
		_method: s, direction: in,
		args: as, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def DisconnectDevice(self, arg_obj_path, *arg, **kw):
		"""
		DisconnectDevice method:
		
		Parameters
		----------
		obj_path: o, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BluetoothStatusChanged(self, *arg, **kw):
		"""
		BluetoothStatusChanged signal:
		
		Parameters
		----------
		arg0: b, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def SetBluetoothStatus(self, arg_status, *arg, **kw):
		"""
		SetBluetoothStatus method:
		
		Parameters
		----------
		status: b, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def QueryPlugins(self, *arg, **kw):
		"""
		QueryPlugins method:
		
		Parameters
		----------
		
		    arg1: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def TransferStatus(self, arg_pattern, *arg, **kw):
		"""
		TransferStatus method:
		
		Parameters
		----------
		pattern: s, direction: in,
		
		    arg2: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def SetTimeHint(self, arg_time, *arg, **kw):
		"""
		SetTimeHint method:
		
		Parameters
		----------
		time: u, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def RfcommDisconnect(self, arg_device, arg_rfdevice, *arg, **kw):
		"""
		RfcommDisconnect method:
		
		Parameters
		----------
		device: s, direction: in,
		rfdevice: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def RfcommConnect(self, arg_device, arg_uuid, *arg, **kw):
		"""
		RfcommConnect method:
		
		Parameters
		----------
		device: s, direction: in,
		uuid: s, direction: in,
		
		    arg3: s, direction: out,
		
		"""
		pass
  
class Introspectable(object):
    '''
    Introspectable
    
    Usage:
    ------
    
    >> myIntrospectable = Introspectable()
    since this you can access any method, attribute or signal defined below this.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myIntrospectable.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myIntrospectable.bar
    >>> myIntrospectable.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myIntrospectable.spam = lambda eggs: do_something(eggs)
    
    '''
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/", "org.blueman.Applet")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Introspect(self, *arg, **kw):
		"""
		Introspect method:
		
		Parameters
		----------
		
		    arg1: s, direction: out,
		
		"""
		pass
  