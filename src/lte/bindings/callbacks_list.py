callback_classes = [
    ['ns3::ObjectBase *', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['bool', 'ns3::Ptr<ns3::NetDevice>', 'ns3::Ptr<const ns3::Packet>', 'unsigned short', 'const ns3::Address &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['bool', 'ns3::Ptr<ns3::NetDevice>', 'ns3::Ptr<const ns3::Packet>', 'unsigned short', 'const ns3::Address &', 'const ns3::Address &', 'ns3::NetDevice::PacketType', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::NetDevice>', 'ns3::Ptr<const ns3::Packet>', 'unsigned short', 'const ns3::Address &', 'const ns3::Address &', 'ns3::NetDevice::PacketType', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::NetDevice>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::MobilityModel>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::SpectrumPhy>', 'ns3::Ptr<const ns3::SpectrumPhy>', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::MobilityModel>', 'ns3::Ptr<const ns3::MobilityModel>', 'double', 'double', 'double', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::SpectrumSignalParameters>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::Packet>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Packet>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned int', 'unsigned int', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Packet>', 'unsigned short', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'std::list<ns3::Ptr<ns3::LteControlMessage>, std::allocator<ns3::Ptr<ns3::LteControlMessage> > >', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'ns3::Ptr<ns3::SpectrumValue>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::DlInfoListElement_s', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::UlInfoListElement_s', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Packet>', 'ns3::Ptr<ns3::SpectrumValue>', 'const std::vector<int, std::allocator<int> > &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::PacketBurst>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::PhyReceptionStatParameters', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::SlPhyReceptionStatParameters', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::LteSpectrumPhy>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'unsigned short', 'double', 'unsigned char', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::PhyTransmissionStatParameters', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'unsigned short', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'unsigned short', 'ns3::LteUePhy::State', 'ns3::LteUePhy::State', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'unsigned short', 'double', 'double', 'unsigned char', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'unsigned short', 'double', 'double', 'bool', 'unsigned char', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'const std::vector<int, std::allocator<int> > &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'unsigned long', 'unsigned int', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Socket>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['bool', 'ns3::Ptr<ns3::Socket>', 'const ns3::Address &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Socket>', 'const ns3::Address &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Socket>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['bool', 'ns3::Ptr<ns3::Packet>', 'const ns3::Address &', 'const ns3::Address &', 'unsigned short', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::EpcUeNas::State', 'ns3::EpcUeNas::State', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::DlSchedulingCallbackInfo', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned int', 'unsigned int', 'unsigned short', 'unsigned char', 'unsigned short', 'unsigned char', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'unsigned char', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'unsigned char', 'unsigned int', 'unsigned long', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'unsigned short', 'ns3::UeManager::State', 'ns3::UeManager::State', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'unsigned short', 'unsigned char', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned short', 'unsigned short', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'unsigned short', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'unsigned short', 'unsigned short', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'unsigned short', 'ns3::LteRrcSap::MeasurementReport', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'unsigned short', 'std::basic_string<char>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned int', 'unsigned int', 'ns3::Ptr<ns3::Packet>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'unsigned short', 'ns3::LteSlDiscHeader', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'unsigned short', 'ns3::LteUeRrc::State', 'ns3::LteUeRrc::State', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::LteUeRrc>', 'std::list<ns3::LteRrcSap::SCellToAddMod, std::allocator<ns3::LteRrcSap::SCellToAddMod> >', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'unsigned short', 'std::basic_string<char>', 'unsigned char', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::LteUeRrc::SlChangeOfSyncRefStatParameters', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned long', 'unsigned short', 'bool', 'unsigned short', 'unsigned short', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned short', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::SpectrumValue &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::ArpCache>', 'ns3::Ipv4Address', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Packet>', 'ns3::Ipv4Address', 'ns3::Ipv4Address', 'unsigned char', 'ns3::Ptr<ns3::Ipv4Route>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Packet>', 'ns3::Ipv6Address', 'ns3::Ipv6Address', 'unsigned char', 'ns3::Ptr<ns3::Ipv6Route>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::Ipv4Header &', 'ns3::Ptr<const ns3::Packet>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::Packet>', 'ns3::Ptr<ns3::Ipv4>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::Ipv4Header &', 'ns3::Ptr<const ns3::Packet>', 'ns3::Ipv4L3Protocol::DropReason', 'ns3::Ptr<ns3::Ipv4>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::Packet>', 'ns3::Ptr<ns3::Ipv6>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::Ipv6Header &', 'ns3::Ptr<const ns3::Packet>', 'ns3::Ipv6L3Protocol::DropReason', 'ns3::Ptr<ns3::Ipv6>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::Ipv6Header &', 'ns3::Ptr<const ns3::Packet>', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'std::basic_string<char>', 'ns3::Ptr<const ns3::Packet>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Packet>', 'ns3::Ipv4Header', 'unsigned short', 'ns3::Ptr<ns3::Ipv4Interface>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ipv4Address', 'unsigned char', 'unsigned char', 'unsigned char', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned int', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<ns3::Packet>', 'ns3::Ipv6Header', 'unsigned short', 'ns3::Ptr<ns3::Ipv6Interface>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ipv6Address', 'unsigned char', 'unsigned char', 'unsigned char', 'unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::TcpRateOps::TcpRateConnection &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'const ns3::TcpRateOps::TcpRateSample &', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::SequenceNumber<unsigned int, int>', 'ns3::SequenceNumber<unsigned int, int>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::TcpSocketState::TcpCongState_t', 'ns3::TcpSocketState::TcpCongState_t', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::TcpSocketState::EcnState_t', 'ns3::TcpSocketState::EcnState_t', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Time', 'ns3::Time', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned char', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'double', 'double', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::TcpSocket::TcpStates_t', 'ns3::TcpSocket::TcpStates_t', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::Packet>', 'const ns3::TcpHeader &', 'ns3::Ptr<const ns3::TcpSocketBase>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['unsigned int', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Time', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::QueueDiscItem>', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::Ptr<const ns3::QueueDiscItem>', 'const char *', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'long', 'long', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'bool', 'bool', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'unsigned int', 'unsigned long', 'unsigned long', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned int', 'unsigned int', 'ns3::LteSlUeRrc::RelayRole', 'ns3::LteSlBasicUeController::Pc5ConnectionStatus', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'std::vector<ns3::SpectrumValue, std::allocator<ns3::SpectrumValue> >', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'unsigned long', 'bool', 'unsigned char', 'unsigned char', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::SlUeMacStatParameters', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
    ['void', 'ns3::SlUeMacStatParameters', 'ns3::LteSlDiscHeader', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty', 'ns3::empty'],
]
