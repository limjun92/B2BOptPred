package com.note.oppty;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.List;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.PumpStreamHandler;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;


@Service
public class OpptyService {
	
	public String getData(OpptyVo opptyVo) {
		String re = "";
		System.out.println("=============================");
		System.out.println("Python Call");
        String[] command = new String[9];
        command[0] = "python";
        //command[1] = "/Users/limju/OneDrive/바탕 화면/신입사원역량강화프로젝트/test.py";
        command[1] = "/Users/limju/OneDrive/바탕 화면/신입사원역량강화프로젝트/oppty_data.py";
        command[2] = opptyVo.getBef1mSlngAmt();
        command[3] = opptyVo.getCircuitNum();
        command[4] = opptyVo.getInvstStgCd();
        command[5] = opptyVo.getXoptyType();
        command[6] = opptyVo.getXtext();
        command[7] = opptyVo.getMarketClassCd();
        command[8] = opptyVo.getCreateMonth();
        try {
        	re = execPython(command);
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println(re);
        return re;
	}
	
	public static String execPython(String[] command) throws IOException, InterruptedException {
		CommandLine commandLine = CommandLine.parse(command[0]);
	    for (int i = 1, n = command.length; i < n; i++) {
	        commandLine.addArgument(command[i]);
	    }

	    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
	    PumpStreamHandler pumpStreamHandler = new PumpStreamHandler(outputStream);
	    DefaultExecutor executor = new DefaultExecutor();
	    executor.setStreamHandler(pumpStreamHandler);
	    int result = executor.execute(commandLine);
	    System.out.println("result: " + result);
	    System.out.println("output: " + outputStream.toString());
	    return outputStream.toString();

	}  
}
