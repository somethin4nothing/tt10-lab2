# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0
# Harry Wu

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_adder(dut):    
    dut._log.info("Starting 8-bit Adder Tests")

    dut.rst_n.value = 0
    await Timer(5, units="ns")
    dut.rst_n.value = 1
    await Timer(5, units="ns")

    # Test Case 1: 5 + 10 = 15
    dut.ui_in.value = 5
    dut.uio_in.value = 10
    await Timer(10, units="ns")
    assert dut.uo_out.value == 15, f"Test failed: 5 + 10 != {dut.uo_out.value}"

    # Test Case 2: 200 + 55 = 255
    dut.ui_in.value = 200
    dut.uio_in.value = 55
    await Timer(10, units="ns")
    assert dut.uo_out.value == 255, f"Test failed: 200 + 55 != {dut.uo_out.value}"

    # Test Case 3: Overflow - 255 + 1 should wrap around to 0 (8-bit behavior)
    dut.ui_in.value = 255
    dut.uio_in.value = 1
    await Timer(10, units="ns")
    assert dut.uo_out.value == 0, f"Test failed: 255 + 1 != {dut.uo_out.value} (Expected 0 due to overflow)"

    # Test Case 4: 0 + 0 = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    await Timer(10, units="ns")
    assert dut.uo_out.value == 0, f"Test failed: 0 + 0 != {dut.uo_out.value}"

    # Test Case 5: 127 + 1 = 128 (Check sign bit transition)
    dut.ui_in.value = 127
    dut.uio_in.value = 1
    await Timer(10, units="ns")
    assert dut.uo_out.value == 128, f"Test failed: 127 + 1 != {dut.uo_out.value}"

    dut._log.info("All test cases passed!")
