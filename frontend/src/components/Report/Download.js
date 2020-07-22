import React from 'react'
import axios from 'axios'
import { Button } from 'antd'
import { DownloadOutlined } from '@ant-design/icons';
const Download = () => {

    const downloadCsv = () => {
        axios({
            url: 'http://localhost:5000/deathteacherbot', //your url
            method: 'POST',
            responseType: 'blob', // important

        }).then((response) => {
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'file.csv'); //or any other extension
            document.body.appendChild(link);
            link.click();
        });
    }


    return (
        <Button type="primary" shape="round" icon={<DownloadOutlined />} onClick={downloadCsv} />
    )
}

export default Download
