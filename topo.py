from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import Host,OVSSwitch, Controller, RemoteController
from mininet.cli import CLI
class SDN(Topo):
    def build (self, **_opts ):
        # Add hosts...
        h1 = self.addHost('h1', ip='10.0.0.1/8', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', ip='10.0.0.2/8', mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', ip='10.0.0.3/8', mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', ip='10.0.0.4/8', mac='00:00:00:00:00:04')

        # Add switches
        s1 = self.addSwitch('s1', cls=OVSSwitch, protocols="OpenFlow13")
        s2 = self.addSwitch('s2', cls=OVSSwitch, protocols="OpenFlow13")
        s3 = self.addSwitch('s3', cls=OVSSwitch, protocols="OpenFlow13")
        # Add links
        self.addLink(h1, s2)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s3)
        self.addLink(s2, s1)
        self.addLink(s3, s1)

def run():
    topo = SDN()
    net = Mininet(topo=topo, controller=None)
    c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1')
    c1.start()
    net.start()
    CLI(net)
    net.stop()
if '_main_':
    setLogLevel( 'info')
    run()
