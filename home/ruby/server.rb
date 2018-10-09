#!/usr/bin/env ruby

require 'eventmachine'
require 'em-websocket'

class ChatConnection < EventMachine::WebSocket::Connection
  def initialize (opts={})
    super

  end
end

EM.run do 
  EM.start_server '0.0.0.0' , 8822 , ChatConnection
end  

p 'server wait on port 8822'
