/*
 * Copyright (c) 2024 Harry WU
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_adder (
    input  wire [7:0] ui_in,    // First 8-bit input
    input  wire [7:0] uio_in,   // Second 8-bit input
    output wire [7:0] uo_out,   // 8-bit output
    output wire [7:0] uio_out,  // Not used
    output wire [7:0] uio_oe,   // Not used
    input  wire       ena,      // Enable signal (ignore)
    input  wire       clk,      // Clock signal (ignore)
    input  wire       rst_n     // Reset signal (ignore)
);

  // 8-bit Adder Logic: uo_out = ui_in + uio_in
  assign uo_out  = ui_in + uio_in;

  // Assign unused output pins to 0
  assign uio_out = 0;
  assign uio_oe  = 0;

  // Prevent warnings by listing unused inputs
  wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule
